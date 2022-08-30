const typography = require('@tailwindcss/typography')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'content/**/*.md',
    'layouts/**/*.html',
    'layouts/work/*.html',
    'layouts/talks/*.html',
    'partials/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [typography],
}
