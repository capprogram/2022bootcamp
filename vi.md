# vi text editor quick start

Last edited by D. Carr - May 2021

Launch the vi text editor by typing `vi filename.txt` into Git Bash. This will open `filename.txt` if it already exists, or create a blank text file with that name.

`vi` launches in the command mode, where you cannot enter text, but can enter vi commands. 

To enter text press `i` to go into insert mode (note `-- INSERT -- ` is displayed at the bottom of the screen. From here you can enter text, move the cursor with the arrow keys, select text, copy and paste with the mouse etc.

To go back to command mode press `ESC`. You can now enter commands (note you must type a leading `:`, as well as press `[Enter]` after the command eg: `:w[Enter]`)

```
:w save (write) the active file
:wq save and quit
:q! quit vi without saving changes
```

This is a very tiny subset of the command you can enter, but should be sufficient for basic editing. For more information

1. `vimtutor` at a terminal will start up an interactive tutorial
2. [A two page printable reference card](http://tnerual.eriogerg.free.fr/vimqrc.pdf)
3. [Vim help in HTML](http://vimhelp.appspot.com/)
