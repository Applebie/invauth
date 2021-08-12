module.exports = {
  runtimeCompiler: true,
  devServer: {
    proxy: {
      '^/users': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure:false,
        pathRewrite: {
          '^/users': ''
        }
      }
    }
  }
}
