
## VIM tricks for characters


- **show all characters that are NOT whitespaces**

`:set list`  
OR  
`:set listchars=eol:$,tab:>-,trail:~,extends:>,precedes:<`


- **show all characters and spaces as well**  
in most recent versions of vim  _(Confirmed on vim 7.4.1689)._

`:set listchars=tab:→\ ,space:·,nbsp:␣,trail:•,eol:¶,precedes:«,extends:»`

- **show non-breaking spaces (NPBS)** as skulls (i.e. something to avoid :)

`:set listchars=nbsp:☠`


---
NOTE: these following 2 need to be tested!

in REGEX world carriage returns are represented using `\r` and line feeds with `\n`.

-  To replace **carriage return character** (which is `<C-m>` or `^M` on M$ Windowz)  
with **line feed character** (which is the break character on *Nix-line OSs) you should check and run the commands in Vim:

`:%s/\r/\n/g`  
`:%s/\n/\r/g`  

Note that in a terminal, `Enter`-key produces `<C-m>` or `^M` too.

-  **To remove ALL carriage return character** from your script ;
within a vim session try:

  `:%s/^M//g`

  Where `^M` in the command above is typed with 2 keystrokes:   
  `[ctrl] + [V] , [ctrl] +[M]`


---

- **show the funky characters** :  
find out what the problematic byte is with `cat -V` or a hexdumper such as `hd` or `xxd`.

  A good common guess is that probably a carriage-return character `0x0d` or `\r` is breaking your code.


---

Ref: [stackOverflow post](https://stackoverflow.com/questions/5939142/replacing-carriage-return-m-with-enter)




