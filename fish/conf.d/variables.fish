set -Ux MICRO_TRUECOLOR 1

set -Ux XDG_CONFIG_HOME $HOME/.config
set -Ux XDG_STATE_HOME $HOME/.local/state
set -Ux XDG_DATA_HOME $HOME/.local/share
set -Ux XDG_CACHE_HOME $HOME/.cache

set -Ux FZF_DEFAULT_OPTS "\
--color=bg+:#313244,bg:#1e1e2e,spinner:#f5e0dc,hl:#f38ba8 \
--color=fg:#cdd6f4,header:#f38ba8,info:#cba6f7,pointer:#f5e0dc \
--color=marker:#b4befe,fg+:#cdd6f4,prompt:#cba6f7,hl+:#f38ba8 \
--color=selected-bg:#45475a \
--multi"

set -Ux GOPATH $XDG_DATA_HOME/go
set -Ux GTK2_RC_FILES $XDG_CONFIG_HOME/gtk-2.0/gtkrc
set -Ux ZDOTDIR $XDG_CONFIG_HOME/zsh
set -Ux CARGO_HOME $XDG_DATA_HOME/cargo
set -Ux CUDA_CACHE_PATH $XDG_CACHE_HOME/nv
set -Ux DOTNET_CLI_HOME $XDG_DATA_HOME/dotnet
