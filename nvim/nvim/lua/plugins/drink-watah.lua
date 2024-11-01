return {
  "mnsdojo/drink-watah.nvim",
  opts = {
    reminder_interval = 45, -- Change interval to 45 minutes
    quiet_hours = {
      enabled = true, -- Enable quiet hours
      start = 22, -- 10 PM
      finish = 8, -- 8 AM
    },
  },
  config = function(_, opts)
    require("drink-watah").setup(opts)
  end,
}
