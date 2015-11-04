import os
import sys
import subprocess
import getopt
import sphinx


def run(*args):
    ret = subprocess.call(args, stdout=sys.stdout, stderr=sys.stderr)
    if ret != 0:
        exit(ret)

def build_docs(source_dir, target_dir, flags):
    """
    Build documentation from ``source_dir``, placing built files in
    ``target_dir``.

    :param str source_dir: location of sphinx documentation files
    :param str target_dir: location to build to
    """
    print 'building documentation'
    args = ['-b html']
    if len(flags):
        args = args + flags
    if sphinx.build_main(args + [source_dir, target_dir]):
        return False
    open('%s/.nojekyll' % target_dir, 'a').close()
    return True

def deploy_docs(target_dir):
    """
    Deploy built docs to gh-pages, uses ``GH_TOKEN`` for pushing built
    documentation files located in *target/doc* to gh

    :param str target_dir: directory that build files were written to
    """
    branch = os.environ['TRAVIS_BRANCH']
    pr = os.environ['TRAVIS_PULL_REQUEST']
    token = os.environ['GH_TOKEN']
    repo = os.environ['TRAVIS_REPO_SLUG']

    if branch == 'master' and pr == 'false':
        print 'uploading docs...'
        sys.stdout.flush()
        run('git', 'clone', 'https://github.com/davisp/ghp-import')
        run('./ghp-import/ghp-import', '-n', 'target/doc/build')
        run('git', 'push', '-fq', 'https://%s@github.com/%s.git'
            % (token, repo), 'master')
    else:
        print 'build triggered for non-master branch \'' + branch + \
                '\', skipping deploy...'

def usage():
    """
    Print usage message when a user does not enter any cline args, or
    if they specify --help
    """
    print 'Usage: travis-sphinx [options] {actions}\n'
    print 'Options:\n  -h, --help\t\tSee usage of script\n' + \
          '  -s, --source\t\tSource directory of sphinx docs, default is docs/source' + \
          '  -n, --nowarn\t\tDo not error on warnings'
    print 'Actions:\n  build \t\tBuild sphinx documentation, places docs in target/doc' + \
          '\n  deploy\t\tDeploy sphinx docs to travis branch by pulling from target/doc'

def main():
    source_dir = 'docs/source'
    target_dir = 'target/doc/build'
    flags = ['-W']
    # Print usage if no arguments entered
    if len(sys.argv) == 1:
        print 'travis-sphinx v0.0.1'
        usage()
        exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'nhs:', ['nowarn', 'help', 'source='])

    except getopt.GetoptError as err:
        print str(err) + ', see --help for valid arguments'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-s', '--source'):
            if sys.argv[-1] == 'deploy':
                print 'source option not allowed for deploy'
                sys.exit(2)
        elif opt in ('-n', '--nowarn'):
            flags.remove('-W')
        source_dir = arg

    if sys.argv[-1] == 'build':
        if not build_docs(source_dir, target_dir, flags):
            exit(2)
    elif sys.argv[-1] == 'deploy':
        deploy_docs(target_dir)
    else:
        usage() 
        exit(2)

if __name__ == '__main__':
    main()
