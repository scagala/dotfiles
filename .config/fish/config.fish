if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -g fish_greeting
set -gx EDITOR micro
#setenv EDITOR micro
#####################################
#               ALIASES             #
#####################################

# SYS
alias ls="exa --oneline --icons --header"
alias la="exa --long --all --icons --no-user --git --octal-permissions --no-permissions --header"
alias ltr="exa --tree --icons"
alias ltd="exa --tree --only-dirs --icons"
# GIT
alias gs="git status"
alias ga="git add"
alias gc="git commit"
alias gp="git push"
alias gpp="git pull"
# OPTIMUS
alias gpu="optimus-manager --print-mode"
alias amd="optimus-manager --switch integrated"
alias nvidia="optimus-manager --switch nvidia"
# coding
alias code="codium"
alias vim="nvim"
