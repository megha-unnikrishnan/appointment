const path = require("path");

module.exports = {
  entry: "./src/plugin.js",
  output: {
    filename: "appointment-plugin.js",
    path: path.resolve(__dirname, "dist"),
    library: "AppointmentPlugin",
    libraryTarget: "umd",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react"],
          },
        },
      },
    ],
  },
};
