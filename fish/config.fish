set -U fish_greeting

fish_ssh_agent
# starship init fish | source
zoxide init fish | source
# oh-my-posh init fish --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/refs/heads/main/themes/amro.omp.json' | source
oh-my-posh init fish --config $HOME/.config/oh-my-posh.omp.json | source
