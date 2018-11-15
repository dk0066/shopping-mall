const APP_ID = 'shopping-mall-app'
const SERVER_URL = 'http://35.220.209.137/parse'

function query(url, data = {}, method = "GET") {
  return new Promise(function (resolve, reject) {
    wx.request({
      url: SERVER_URL + url,
      data: data,
      method: method,
      header: {
        'Content-Type': 'application/json',
        'X-Parse-Application-Id': 'shopping-mall-app'
      },
      success: function (response) {
        console.log("success");
        console.log(response);
        if (response.statusCode == 200) {
          resolve(response.data.results);
        }
        else {
          reject(response.errMsg);
        }
      },
      fail: function (err) {
        reject(err)
        console.log("failed")
      }
    })
  });
}

function queryHome() {
  return query('/classes/Home');
}

function queryBanner() {
  console.log("Fetch banner from parse server.")
  return query('/classes/Banner');
}

function queryCatalog(parentId = 0, limit=0) {
  return query('/classes/Catalog' + (limit > 0 ? '?limit=' + limit : ''))
}

function queryGoods(constraints={}, page={}) {
  const limit = page['limit'] || 0;
  const skip = page['skip'] || 0;
  const order = page['order'] || 'updateAt';
  const url = '/classes/Goods?where=' + encodeURI(JSON.stringify(constraints)) + '&order=' + order + '&limit=' + limit + '&skip=' + skip;

  console.log("Fetch goods from " + url)

  return query(url);
}

module.exports = {
  queryHome,
  queryBanner,
  queryCatalog,
  queryGoods
}
