nnoremap <f1> :set hls <CR>
"nnoremap <f2> :split term://zsh <CR>
nnoremap <f2> :term <CR>
nnoremap <f3> :UndotreeToggle <CR>
nnoremap <f4> :NERDTreeToggle<CR>
nnoremap <C-z> :vertical split<CR>
nnoremap <S-x> :vertical resize +5<CR>
nnoremap <C-x> :vertical resize -5 <CR>
nnoremap <C-q> :GitGutterToggle<CR>
nnoremap <leader>b :Buffers <CR>
nnoremap <leader>h :wincmd h <CR>
nnoremap <leader>j :wincmd j <CR>
nnoremap <leader>k :wincmd k <CR>
nnoremap <leader>l :wincmd l <CR>
"nnoremap <leader>f2 :set autochdir <CR>
inoremap <C-s>  <ESC>:w <CR>
nnoremap <C-s> :w <CR>
"fuzzy finding mappings 
nnoremap<C-t> :Files <CR>
nnoremap<C-p> :Rg <CR>
" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" Using lua functions
nnoremap <leader>ff <cmd>lua require('telescope.builtin').find_files({hidden=true})<cr>
nnoremap <leader>fg <cmd>lua require('telescope.builtin').live_grep()<cr>
nnoremap <leader>fb <cmd>lua require('telescope.builtin').buffers()<cr>
nnoremap <leader>fh <cmd>lua require('telescope.builtin').help_tags()<cr>

nnoremap<leader>gc :Git commit <CR> 
nnoremap<leader>gch :Git checkout
"nnoremap<leader>gd :Git diff<CR> 
nnoremap<leader>gw :Gvdiffsplit<CR> 
nnoremap<leader>gs :G<CR>
nnoremap<leader>gp :Git push<CR>
nnoremap<leader>g1 :diffget //2<CR>
nnoremap<leader>g0 :diffget //3<CR>
nnoremap<C-a> ggVG 


"easy align commands
" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)
" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)
