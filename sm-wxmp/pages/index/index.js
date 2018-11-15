const util = require('../../utils/util.js');
const api = require('../../config/api.js');
const user = require('../../services/user.js');
const Parse = require('../../utils/parse.js');

//获取应用实例
const app = getApp()

Page({
  data: {},
  onShareAppMessage: () => {
    return {
      title: 'Tomato Mall',
      desc: '全球货物，触手可及 - 蕃茄 Tomato Mall',
      path: '/pages/index/index'
    }
  },
  onLoad: function(options) {
    let self = this;
    Parse.queryHome().then(result => self.setData(result[0]));
  },
  onReady: function() {
    // 页面渲染完成
  },
  onShow: function() {
    // 页面显示
  },
  onHide: function() {
    // 页面隐藏
  },
  onUnload: function() {
    // 页面关闭
  },
})
