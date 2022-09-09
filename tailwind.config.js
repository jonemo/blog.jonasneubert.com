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
    fontFamily: {
      sans: [
        'Quicksand',
        'Century Gothic',
        'AppleGothic',
        'ui-sans-serif',
        'system-ui',
        'Helvetica',
        'sans-serif',
      ],

      monospace: ['Cutive Mono', 'monospace'],
    },

    extend: {
      color: {
        red: {
          600: '#c40d0b',
        },
        yellow: {
          600: '#ffe400',
        },
      },

      typography: (theme) => ({
        DEFAULT: {
          css: {
            code: {
              backgroundColor: theme('colors.gray.100'),
              color: theme('colors.gray.800'),
              fontWeight: '400',
              'border-radius': '0.25rem',
            },
            'code::before': {
              content: '""',
              'padding-left': '0.25rem',
            },
            'code::after': {
              content: '""',
              'padding-right': '0.25rem',
            },
          },
        },
      }),
    },
  },
  plugins: [typography],
}
