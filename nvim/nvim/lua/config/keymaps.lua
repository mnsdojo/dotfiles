-- Existing keymaps
vim.keymap.set("n", "Y", "y$", { desc = "Yank to the end of the line" })
vim.keymap.set(
  "n",
  "<leader>sx",
  require("telescope.builtin").resume,
  { noremap = true, silent = true, desc = "Resume" }
)

-- Copy all to clipboard (Q)
vim.keymap.set("n", "Q", function()
  vim.cmd('normal! ggVG"+y')
  vim.notify("Copied entire file to clipboard", vim.log.levels.INFO)
end, { desc = "Copy entire file to clipboard" })

-- Delete all content (D)
vim.keymap.set("n", "D", function()
  local line_count = vim.api.nvim_buf_line_count(0)
  vim.cmd("normal! ggdG")
  vim.notify("Deleted " .. line_count .. " lines", vim.log.levels.INFO)
end, { desc = "Delete entire file content" })
