#!/usr/bin/python

import sys
import git


def getCommitList(repoPath, srcCommit, dstCommit):
	try:
		repo = git.Repo(repoPath)
	except:
		print "Repo path is incorrect"
	commits = []
	try:
		for commit in repo.iter_commits(rev=src+"..."+dst):
			commits.append((commit.binsha.encode('hex_codec'),commit.message))
			print "Commit: ", commit.binsha.encode('hex_codec')

	except git.GitCommandError as err:
	    print "One of the provided commit can't be found"

	return commits

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print "help"
		quit(1)

	path = str(sys.argv[1])
	src = str(sys.argv[2])
	if len(sys.argv) == 4:
		dst = str(sys.argv[3])
	else:
		dst = "HEAD"

	print path , src, dst
	commits = getCommitList(path , src, dst)
