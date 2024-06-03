


var map = L.map("map").setView([50.8484, 5.6888], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);






L.marker([50.8387222, 5.7121196])
    
    .addTo(map)
    .bindTooltip("<strong>Forum 100, 6229 GV Maastricht</strong><br>MECC");
    




L.marker([50.8449465, 5.6848629])
    
    .addTo(map)
    .bindTooltip("<strong>Tongersestraat 53, 6211 LM Maastricht</strong><br>School of business and economics maastricht");
    













L.polygon([[47.81025552661079, 19.02201563177881],[47.80993848992647, 19.024740756084967],[47.812863800415236, 19.026607573523037],[47.811667757419514, 19.038366377615738],[47.804750341957295, 19.035233557547244],[47.80770476752536, 19.021672309031583]], {color: '#ff6b6b'})
    
    .addTo(map)
    .bindTooltip("This is a tooltip with no title...<br>...and with multiple lines of text", {direction: 'center', offset: L.point({x: 0, y: 0})});
    


