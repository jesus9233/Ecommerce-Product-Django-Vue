const GoogleFontsPlugin = require("google-fonts-webpack-plugin")

module.exports = {
   configureWebpack: {
    plugins: [
          new GoogleFontsPlugin({
              fonts: [
                  { family: "Poppins", variants: ["600", "700"] },
                  { family: "Roboto", variants: [ "400", "500", "700" ] }
                  { family: "Pacifio" }
              ]
          })
      ]
    }
}
console.log('okkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
