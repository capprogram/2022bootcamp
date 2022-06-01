| [⬅ 1. Automated Version control](01-automated-version-control.md) | [Table of Contents](00-contents.md) | [3. Tracking changes ➡](03-tracking-changes.md) |
| :---- |:----:| ----:|


# 2. Creating a Repository

Assuming Git is configured, we can start using it. Note that Git uses the Bash coding language, and we will employ simple commands in that language. Here is a small list of some basic commands that will come up a lot during the entire git tutorial that aren't git-specific:

  `mkdir [name]` = will make a directory called [name]
  
  `rmdir [name]` = will remove a directory called [name] assuming it is empty

  `cd [path]` = will change your current directory into the one called [path], can also put in an absolute path such as /users/documents/[name]
  
  `cd ..` = will send you one directory up

  `ls` = list the contents of the current directory
  
  `cat [filename]` = prints out the contents of filename into the terminal

Let's create a directory for our work and then move into that directory:
```
$ mkdir planets
$ cd planets
```

Then we tell Git to make `planets` a repository—a place where
Git can store versions of our files:
```
$ git init
```

If we use `ls` to show the directory's contents,
it appears that nothing has changed:
```
$ ls
```

But if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory within `planets` called `.git`:
```
$ ls -a
.	..	.git
```

Git stores information about the project in this special sub-directory.
If we ever delete it,
we will lose the project's history.

We can check that everything is set up correctly
by asking Git to tell us the status of our project:

```
$ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```

## Places to Create Git Repositories

Dracula starts a new project, `moons`, related to his `planets` project.
Despite Wolfman's concerns, he enters the following sequence of commands to
create one Git repository inside another:

```
cd             # return to home directory
mkdir planets  # make a new directory planets
cd planets     # go into planets
git init       # make the planets directory a Git repository
mkdir moons    # make a sub-directory planets/moons
cd moons       # go into planets/moons
git init       # make the moons sub-directory a Git repository
```

Why is it a bad idea to do this?
How can Dracula undo his last `git init`?

WARNING: Do not use "git clean" or "rm * " -- these are very dangerous commands!
There's just one file you need to delete at this point. (Hint: it starts with ".".)
