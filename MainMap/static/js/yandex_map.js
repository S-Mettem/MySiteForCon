/*
  Yandex Map with all points
    More information:
      https://tech.yandex.ru/maps/jsapi/doc/2.1/quick-start/index-docpage/#create_map_container

*/
ymaps.ready(function(){
  // Create map
  var MyMap = new ymaps.Map("map", {
    center:[55.01286117, 82.92154831],
    zoom: 11,
  })
});
