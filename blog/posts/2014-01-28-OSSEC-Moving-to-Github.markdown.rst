.. post:: Jan 1, 2014
   :tags: git, hg, development
   :category: Announcements
   :author: Vic Hargrave

======================
OSSEC Moving to Github
======================


OSSEC is moving from bitbucket to github, and in the process moving to a
new method for accepting contributions. This is an exciting change that
we feel will help push OSSEC forward in 2014 and further into the
future.

-  `oRFC:1 Collective Code Construction
   Contract <https://github.com/ossec/ossec-docs/blob/master/docs/oRFC/orfc-1.rst>`__
   (Adapted from ZeroMQ's `C4 <http://rfc.zeromq.org/spec:22>`__).

The overall goals of the change are to allow OSSEC to be more dynamic,
agile, and quicker to respond to the needs of the community.

This change will not be without issues or problems, but we aim to make
it as seamless as possible. To do this we are committing to the
following task to be completed 7 days from now:

1. Port all code to github
2. Port all Open Issues to github issues
3. Port all Open Pull Requests to github Pull Requests

1) Porting code
~~~~~~~~~~~~~~~

This is currently done every 30 minutes (when hg-git does not break). We
have set up and enabled `github.com/ossec/ossec-hids <>`__

This will continue till to the cut over date of Feb 7th 2014.

2) Port all Open Issues
~~~~~~~~~~~~~~~~~~~~~~~

We will copy all open issues from Bitbucket to github. Due to the api
available, and reporting user and all comments on issues will show up as
the user performing the migration. Test runs are being preformed to
`githib.com/jrossi/issue-migration-test <>`__

3) Port all Open Pull Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This process will be the hardest, and will be the hardest to detail, but
we shall attempt it here.

Contact pull request author to request they move to github and resubmit
using github. If no response is received before the following:

-  Create github.com/ossec/bitbucket-pull-requests as a fork of
   github.com/ossec/ossec-hids/
-  Export each Pull Request as a patch bb-gh-pull-request-##.patch
-  Import each patch into a branch named bb-gh-pull-request-##

   -  Apply correct author/email git information so no information is
      lost.

-  Create a github pull request for each branch.

For authors who email addresses match between githib and bitbucket
everything will show up as expected. Authors can also use github email
settings to add second or third email address.

Once completed, each pull request will stand on its own and be reviewed
for merging based on the Collective Code Construction Contract.
