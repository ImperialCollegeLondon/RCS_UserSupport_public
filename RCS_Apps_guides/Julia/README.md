
### Using Julia via module files on the HPC


```
$ module avail julia
---------------------------------------------------------------------------- /apps/modules/4.7.1/modulefiles -----------------------------------------------------------------------------
julia/0.3.11 julia/0.5.0 julia/0.5.0-common(default) julia/0.6.1 julia/0.6.2 julia/1.6.0

$ module show julia/1.6.0
```
--> please make sure that the PKG directory is pointing towards your `$HOME/.julia`  folder  
(which may be already present or may need to be created/deleted accordingly perhaps)


##### example of workflow

NOTES:
- **NOT to be run on LOGIN NODES** but in **JOB-SCRIPTS!**
- see notes below and documents on job-scripts.

##### **workflow_1** :

```
$ module load julia/1.6.0

$ which julia

$ julia --version

$ julia
```

once the "julia command-line prompt" loads `julia>` you can run Julia commands :

---


##### examples:


check env setup :

```
julia> Base.load_path()
julia> Base.DATAROOTDIR
julia> Sys.BINDIR
```

install packages :    
(please do NOT run this on the HPC unless you know what you're doing and "where" exactly these ops will have effect)

```
julia> using Pkg
julia> Pkg.add("JuMP")
```

to get help:   

 `julia> ?`

output:

```
help?>
search:  ] [ = $ ; ( { ) ? . } ⊻ ⊋ ⊊ ⊉ ⊈ ⊇ ⊆ ≥ ≤ ≢ ≡ ≠ ≉ ≈ ∪ ∩ ∛ √ ∘ ∌ ∋ ∉ ∈ ℯ π ÷ ~ | ^ \ > < : / - + * ' & % ! && if :: [] ?: {} () || do .= IO |> rm pi mv in im fd cp cd GC >> >= >: => == <= << <: // != new let end try ... for

  Welcome to Julia 1.6.4. The full manual is available at

  https://docs.julialang.org

  as well as many great tutorials and learning resources:

  https://julialang.org/learning/

  For help on a specific function or macro, type ? followed by its name, e.g. ?cos, or ?@time, and press enter. Type ; to enter shell mode, ] to enter package mode.

julia>

```

NOTES:

- we advise users not to "play around" too much with packages and customization/installations especially if they are new to the HPC and the software.
- use anaconda virtual environments if you need to install custom Packages.(see other guides in this repo)


**IMPORTANT:**  

please note that following **workflow_1** above will result in user **running the software on the login node** (i.e. the node where they land when connecting to the HPC.) and this is normally not allowed.

this is allowed ONLY for quick testing work and/or short not computationally intensive workflows (e.g. quick debugging etc.)

for anything else please refer to **job-sizing guidance** and submission of proper job-scripts that runs your software of choice on the compute nodes.
