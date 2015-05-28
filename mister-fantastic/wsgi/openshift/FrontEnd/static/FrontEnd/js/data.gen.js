a = {"project":{"teams":[{"id":1,"name":"default"},{"id":2,"name":"Dream Team"}],"programmers":[{"id":1,"name":"Igor Finagin","team":2},{"id":2,"name":"Dinar Kalimullin","team":2},{"id":3,"name":"Artur Muhametov","team":1},{"id":4,"name":"Nikita Tihonov","team":1}],"commits":[]}};

function random(a,b){
    return Math.round(Math.random()*(a|1))+(b|0);
}


var time = new Date().getTime();
var d;

for(var i = 0; i < 10; i++){
    d = new Date(time);
    YYYY = d.getFullYear();
    MM = (((d.getMonth() + 1) < 10) ? '0' : '') + (d.getMonth() + 1);
    DD = ((d.getDate() < 10) ? '0' : '') + d.getDate();
    
    for(var j = 0, k = a.project.programmers.length; j < k; j++){
        if(random(100)>20){
            if(random(100)<13){
                a.project.commits.push({
                    "programmer": j+1,
                    "date": YYYY + "-" + MM + "-" + DD,
                    "new": 0,
                    "del": random(500,300)
                });
            } else {
                a.project.commits.push({
                    "programmer": j+1,
                    "date": YYYY + "-" + MM + "-" + DD,
                    "new": random(250,150),
                    "del": random(190,10)
                });
            }
        }
    }
    time -= 1000 * 60 * 60 * 24;
}
a.project.commits.reverse();

JSON.stringify(a);