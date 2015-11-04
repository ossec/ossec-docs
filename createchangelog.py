from github3 import login


gh = login(token="d25196ce55a7b7a8ed01a5fe027d706b79ce4c6a")
repo =  gh.repository("ossec", "ossec-hids")

allPulls = []
for pull in repo.iter_pulls(state="closed"):
    allPulls.append(pull)

allReleases = []
for release in repo.iter_releases():
    allReleases.append(release)

allTags = []
for tag in repo.iter_tags():
    allTags.append(tag)
