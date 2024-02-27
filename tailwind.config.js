module.exports = {
  content:["./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        secondary: '#96EF1D',
        dark: '#0C0E12',
        light: 'white',
        lightGray: '#a0a0a0'
      },
      fontFamily: {
        Onest: ["Onest", "sans-serif"],
      },
      backgroundImage: {
        'pattern': "url('/src/assets/Image/login_image.jpg')",
      },
    },
  },
  plugins: [],
}