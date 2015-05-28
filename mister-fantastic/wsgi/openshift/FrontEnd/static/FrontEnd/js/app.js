			angular.module('MisterFantastic', ['ngRoute', 'angularCharts'])
			
			.config(['$interpolateProvider', function($interpolateProvider) {
				$interpolateProvider.startSymbol('{$');
				$interpolateProvider.endSymbol('$}');
			}])

			.config(['$routeProvider', function($routeProvider){
				$routeProvider
				.when('/project', {
					controller:'ProjectCtrl',
					templateUrl:'/static/FrontEnd/js/templates/project.html'
				})
				.when('/team', {
					controller:'TeamCtrl',
					templateUrl:'/static/FrontEnd/js/templates/team.html'
				})
				.when('/programmer', {
					controller:'ProgrammerCtrl',
					templateUrl:'/static/FrontEnd/js/templates/programmer.html'
				})
				.when('/login', {
					controller:'LoginCtrl',
					templateUrl:'/static/FrontEnd/js/templates/login.html'
				})
				.when('/moderation', {
					controller:'ModerCtrl',
					templateUrl:'/static/FrontEnd/js/templates/moderation.html'
				})
				.otherwise({
					redirectTo:'/login'
				});
			}])

			.value(
				'Dictionary',
				{
					'txtDesc': [
						'Statistics of your Git repositories',
						'Статистика Ваших Git репозиториев'
					],
					'inpLink': [
						'Link to Git repository',
						'Ссылка на Git репозиторий'
					],
					'inpUser': [
						'User',
						'Пользователь'
					],
					'inpPass': [
						'Password',
						'Пароль'
					],
					'inpStart': [
						'Start scanning',
						'Начать сканирование'
					],
					'titleLang': [
						'Сменить язык',
						'Change language'
					],
					'menuProject': [
						'About project',
						'О проекте'
					],
					'menuTeams': [
						'About teams',
						'О командах'
					],
					'menuProgrammer': [
						'About programmers',
						'О разработчиках'
					],
					'programmerSelector': [
						'Choose programmer',
						'Выберите программиста'
					],
					'teamSelector': [
						'Choose team',
						'Выберите команду'
					],
                    'moderTitle': [
                        'The repository has been sent for moderation.',
                        'Репозиторий отправлен на модерацию.'
                    ],
                    'moderText': [
                        'Moderation takes place during the day. After this time you will get access to the statistics of the repository.',
                        'Модерация проходит в течении суток. По истечению этого времени Вы получите доступ к статистике репозитория.'
                    ]
				}
			)

			.factory('$getData', ['$http', function($http){
				return function(url, params, callback){
					$http({url:'static/FrontEnd/js/data.big.json', method:'GET'}).success(callback);
				};
			}])
            
            .factory('draw', [function(){
                return function(DATA){
                    var chart = AmCharts.makeChart("chartdiv", {
                        "type": "serial",
                        "theme": "patterns",
                        "pathToImages": "http://www.amcharts.com/lib/3/images/",
                        "dataDateFormat": "YYYY-MM-DD",
                        "valueAxes": [{
                            "id": "v1",
                            "axisAlpha": 0,
                            "position": "left"
                        }, {
                            "id": "v2",
                            "axisAlpha": 0,
                            "position": "left"
                        }],
                        "graphs": [{
                            "id": "g1",
                            "balloonText": "New [[value]] lines",
                            "lineColor": "#009900",
                            "bullet": "round",
                            "bulletBorderAlpha": 1,
                            "bulletColor": "#00ff00",
                            "bulletSize": 5,
                            "hideBulletsCount": 50,
                            "lineThickness": 2,
                            "title": "red line",
                            "useLineColorForBulletBorder": true,
                            "valueField": "new"
                        }, {
                            "id": "g2",
                            "balloonText": "Del [[value]] lines",
                            "lineColor": "#cc0000",
                            "bullet": "round",
                            "bulletBorderAlpha": 1,
                            "bulletColor": "#ff0000",
                            "bulletSize": 10,
                            "hideBulletsCount": 50,
                            "lineThickness": 2,
                            "title": "red line",
                            "useLineColorForBulletBorder": true,
                            "valueField": "del",
                            "type": 'smoothedLine'
                        }],
                        "chartScrollbar": {
                            "graph": "g1",
                            "scrollbarHeight": 30
                        },
                        "chartCursor": {
                            "cursorPosition": "mouse",
                            "pan": true,
                            "valueLineEnabled": true,
                            "valueLineBalloonEnabled": true
                        },
                        "categoryField": "date",
                        "categoryAxis": {
                            "parseDates": true,
                            "dashLength": 1,
                            "minorGridEnabled": true,
                            "position": "top"
                        },
                        "dataProvider": DATA
                    });

                    chart.addListener("rendered", zoomChart);

                    zoomChart();

                    function zoomChart() {
                        chart.zoomToIndexes(chart.dataProvider.length - 10, chart.dataProvider.length - 1);
                    }
                };
            }])
            
            .factory('summ', [function(){
                return function(a){
                    var res = [0,0,0];
                    
                    for(var i = 0, l = a.length; i < l; i++){
                        res[0] += a[i].new;
                        res[1] += a[i].del;
                    }
                    res[2] = res[0] - res[1];
                    
                    return res;
                }
            }])

			.controller('MainCtrl', ['$scope', '$rootScope', '$location', 'Dictionary', function($scope, $rootScope, $location, Dictionary){
                $scope.lang = 1;
				$scope.changeLang = function(){
					$scope.lang = ($scope.lang + 1) % 2;
				}
				$scope.hideMenu = function(bool){
					return ($location.path() === '/login' || $location.path() === '/moderation');
				};
				$scope.dic = Dictionary;
			}])
			
			.controller('LoginCtrl', ['$scope', function($scope){

            }])
			
			.controller('ModerCtrl', ['$scope', function($scope){
                
            }])
			
			.controller('ProjectCtrl', ['$scope', '$getData', function($scope, $getData){
				$getData('static/data.big.json', {}, function(data){$scope.project = data.project})
			}])
			
			.controller('TeamCtrl', ['$scope', '$getData', 'draw', 'summ', function($scope, $getData, draw, summ){
                function commits(id){
                    var team = [],
                        temp = [],
                        res = [];
                    
                    for(var i = 0, l = $scope.project.programmers.length; i < l; i++){
                        if($scope.project.programmers[i].team == id){
                            team.push($scope.project.programmers[i].id);
                        }
                    }
                    for(var i = 0, l = $scope.project.commits.length; i < l; i++){
                        if(team.indexOf($scope.project.commits[i].programmer) >= 0){
                            res.push($scope.project.commits[i]);
                        }
                    }
                    
                    temp.push(res[0])
                    for(var i = 1, l = res.length; i < l; i++){
                        if(res[i].date == temp[temp.length-1].date){
                            temp[temp.length-1].del += res[i].del;
                            temp[temp.length-1].new += res[i].new;
                        } else {
                            temp.push(res[i]);
                        }
                    }
                    
                    return temp;
                }
				$getData('static/data.big.json', {}, function(data){
                    $scope.project = data.project;
                    $scope.$watch('teams', function(a){
                        if(a){
                            draw(commits($scope.teams.id));
                            $scope.nums = summ(commits($scope.proger.id));
                        }
                    })
                })
			}])
			
			.controller('ProgrammerCtrl', ['$scope', '$getData', 'draw', 'summ', function($scope, $getData, draw, summ){
                function commits(id){
                    var res = [];
                    for(var i = 0, l = $scope.project.commits.length; i < l; i++){
                        if($scope.project.commits[i].programmer == id){
                            res.push($scope.project.commits[i]);
                        }
                    }
                    return res;
                }
				$getData('static/frontend/js/data.big.json', {}, function(data){
                    
                    $scope.project = data.project;
                    $scope.$watch('proger', function(a,b){
                        if(a){
                            draw(commits($scope.proger.id));
                            $scope.nums = summ(commits($scope.proger.id));
                        }
                    })
                });
            }])