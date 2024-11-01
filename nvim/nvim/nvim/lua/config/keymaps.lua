-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set("n", "Y", "y$", { desc = "Yank to the end of the line" })

vim.keymap.set("n", "Q", function()
  vim.api.nvim_command("normal! ggVGy")
  vim.notify(
    "Text copied to clipboard",
    vim.log.levels.INFO,
    { title = "Selection Copied" }
  )
end, { desc = "Select all and copy to clipboard" })

-- Add delete all keymap
vim.keymap.set("n", "D", function()
  vim.api.nvim_command("normal! ggVGd")
  vim.notify(
    "All text deleted",
    vim.log.levels.INFO,
    { title = "Buffer Cleared" }
  )
end, { desc = "Delete all text in buffer" })

vim.keymap.set(
  "n",
  "<leader>sx",
  require("telescope.builtin").resume,
  { noremap = true, silent = true, desc = "Resume" }
)
