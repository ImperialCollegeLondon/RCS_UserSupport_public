
## GIT

the simplest way to use git is to run the following workflow:


1. create a folder to store your code:  
```
mkdir my_CodeProject
cd my_CodeProject
```

2. initialise the folder as a git source-controlled repository:  
`git init`  

3. perform coding operations, files/folders creations etc...  

```
<create code files 1,2,3>
<modify code files ...>
<create new sub-folder>
```

4. check the status of the repo this will show staged files (green), untracked files (red) etc..

`git status`  

5. once happy with code files and mods stage the files (prepare them to be commited to your local repo)

stage multiple single files:  
```
git add file_1
git add file_2
git add file_3
```

OR alternatively: stage multiple files at once  
`git add file_1 file_2`  

OR alternatively: stage all modified files at once   
`git add .`  

if you have deleted files (e.g. from previous commits you can use the `--all` flag); this will report files as deleted/modified.

`git add --all .`

5. once happy with code files and mods staged commit them.

(note if you change your mind now and re-modify files you will need to stage/add them back)

`git commit -m "a short descriptive message here"`


**TIPS :**  
- keep the commit message short and meaningful of your operations.      
- avoid funky chars and punctuations in the message   


that's it for the time being!

---

## more advanced concepts.

#### code branches:

- list available code branches:

`git branch -la`  

- to create a new branch (a part from the baseline code in "main" or "master" branch)
(this is useful to test features and code modifications without affecting your mainline code)

`git checkout -b branchname`

(e.g. `git checkout -b development`)

will start a parallel new branch called development in this case and put you in that one.. every mod you do here will be stored in this new branch.


<!-- more stuff on branches rebasing etc..-->


### References



[simple online guide on git](https://rogerdudler.github.io/git-guide/)  
[Git code swcarpentries](https://swcarpentry.github.io/git-novice/)  