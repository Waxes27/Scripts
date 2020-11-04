# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    read -p "git commit(what activity you working on)? leave empty for no commit message:  " git
    #read -s -p "Keycloak password:    " password
    #password ="password"
    read -p "Exercise UUID:    " uuid
    clear
    #if [$git == 'Toy Robot 3']; then
    #    $uuid='8dea9e69-07da-440d-964c-08e868e11561'
    #fi
    echo $git $uuid

    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias register="wtc-lms register"
    alias problems="cd ~/problems/"
    alias bashrc="gedit ~/.bashrc"
    alias g="stored;sleep 4;git add . && git commit -m '$git' && git push;wtc-lms save $uuid;sleep 4;exit;exit;exit"
    alias s="wtc-lms save $uuid;sleep 4; echo 'PRESS CTRL+C TO CANCEL EXIT SEQUENCE';sleep 4;exit;exit;exit"
    alias grade="wtc-lms grade $uuid; h; echo 'PRESS CTRL+C TO CANCEL EXIT SEQUENCE';sleep 4;exit;exit;exit"
    alias start="logins;wtc-lms start $uuid; problems; code ."
    alias h="wtc-lms history $uuid"
    alias test="python3 -m unittest tests/test_main.py"
    alias stored="wtc-lms config;echo 'commit message is: $git
    

exercise uuid: $uuid'"
    alias wtc-lms="~/Downloads/wtc-lms"
    alias alles="logins;stored;sleep 3;g;s;grade"
    #alias wtcl=""$password" && sleep 3| wtc-lms login"
    alias logins="wtc-lms login $password;register;stored"
    alias fundamentals="wtc-lms topics 505079ba-4393-47ff-a956-330555b09f00"

    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias virtual="cd ~/wtc-tdd-workshop && source .venv/bin/activate"
alias janet="mv ~/.config/wtc/config.yml ~/.config/wtc/config.ym0; mv ~/.config/wtc/config.ym ~/.config/wtc/config.yml; mv ~/.config/wtc/config.ym0 ~/.config/wtc/config.ym; wtc-lms config; logins"

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
PATH=/bin:$PATH
#PATH=/bin:/bin:/home/c4r5s3/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:~/bin/VSCode-linux-x64/bin
#PATH=~/bin:/bin:/bin:/home/c4r5s3/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/c4r5s3/bin/VSCode-linux-x64/bin:~/bin/VSCode-linux-x64/bin
#PATH=~/bin:/home/c4r5s3/bin:/bin:/bin:/home/c4r5s3/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/c4r5s3/bin/VSCode-linux-x64/bin:/home/c4r5s3/bin/VSCode-linux-x64/bin:~/bin/VSCode-linux-x64/bin
