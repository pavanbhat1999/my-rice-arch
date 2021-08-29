call plug#begin('~/.vim/plugged')
Plug 'mbbill/undotree'
"directory structure plugin"
Plug 'scrooloose/nerdtree'
"vim fugitive for git logs
Plug 'tpope/vim-fugitive'
"multiple cusrsors like sublime"
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
"auto completion of pairs"
Plug 'jiangmiao/auto-pairs'
"commentor"
Plug 'scrooloose/nerdcommenter'
"adding icons
Plug 'ryanoasis/vim-devicons'
Plug 'kyazdani42/nvim-web-devicons'
"startup script for vim
Plug 'mhinz/vim-startify'
"git-gutter
Plug 'airblade/vim-gitgutter'
"intelliscense
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
"__________________________________________________
Plug 'neovim/nvim-lspconfig'
" Install nvim-cmp
Plug 'hrsh7th/nvim-cmp'
" Install the buffer completion source
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/vim-vsnip'
Plug 'hrsh7th/vim-vsnip-integ'
"icons for lsp
Plug 'onsails/lspkind-nvim'
"__________________________________________________
"surroundings
Plug 'tpope/vim-surround'
"color-scheme
Plug 'tpope/vim-vividchalk'
"indentation guidelines
"Plug 'nathanaelkane/vim-indent-guides'
Plug 'Yggdroot/indentLine'
""minimap
"Plug 'wfxr/minimap.vim'
Plug 'psliwka/vim-smoothie'
"status line
Plug 'vim-airline/vim-airline'
"css-color support
"Plug 'ap/vim-css-color'
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }
"Plug 'glepnir/galaxyline.nvim' , {'branch': 'main'
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
""fuzzy finedr using fzf
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
"auto closing tags - web development
Plug 'alvan/vim-closetag'
"color picker for vim
Plug 'KabbAmine/vCoolor.vim'
"notes for vim
Plug 'vimwiki/vimwiki'
"easr align
Plug 'junegunn/vim-easy-align'
"tree sitter for better syntax highlighting
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
"latex completion
Plug 'lervag/vimtex'
call plug#end()
