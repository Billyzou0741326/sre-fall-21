module.exports = {
  purge: {
    enabled: true,
    content: ['./templates/**/*.html'],
  },
  darkMode: false, // or 'media' or 'class'
  mode: 'jit',
  theme: {
    minWidth: {
      '0': '0',
      '1/4': '25%',
      '1/2': '50%',
      '3/4': '75%',
      'full': '100%',
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
