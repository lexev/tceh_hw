//1. Написать функцию для определения НОК для двух чисел.
function nok(a, b) {

    var m = a * b
    while (a!=0 && b!=0) {
        if (a > b) a = a % b
        else b = b % a
    }
    return m // (a + b)
    }

/*
2. Написать функцию, которая принимает список, и возвращает словарь в формате:
"тип данных: количество объектов"
 */
function counttyp(lst) {
    var objectTypes = {number: 0, string: 0, object: 0};
    lst.forEach(function(item, i, lst) {
        if (typeof(item) in objectTypes){
            objectTypes[typeof(item)] = objectTypes[typeof(item)] + 1;
            }});
    return objectTypes;}


/*
3. Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей
 */
function eq_key(dict1, dict2){
    var count = 0;
    Object.keys(dict1).forEach(function(i){
        if (i in dict2){
            count++;
        }
    })
    return count;
}


/*
4. Написать функцию, которая принимает любое количество аргументов,
она должна вернуть список типов, принятых аргументов
 */

function types_of_args(){
    var types = [];
    var resultList = [];

    for (var i = 0; i < arguments.length; i++) {
        types.push(typeof(arguments[i]));
        }
     types.forEach(function (item) {
        if (!(~resultList.indexOf(item))) {
            resultList.push(item)
        }})
   return resultList;
}


/*
5. Написать функцию, которая принимает на вход список списков (матрицу) и выводит ее в виде матрицы
(один ряд на одной строке) в консоль
 */

function pMatr(matr) {
    for (var row in matr) {
        console.log(matr[row].join(' '));
    }
}



/*
6. Написать функцию, которая принимает любое количество аргументов - списков, она должна возвращать список из всех объектов списков,
 но каждый объект должен быть уникальным
 */
function List_of_list(lsts){
    var lst = [];
    var rlt_lst = [];
    lsts.forEach(function (lsts_item) {
        lsts_item.forEach(function(lst_item){
        lst.push(lst_item)
        })
    })
    lst.forEach(function (item) {
        if (!(~rlt_lst.indexOf(item))){
            rlt_lst.push(item)
        }

    })
    console.log(rlt_lst)
}


console.log(nok(5,6))
var dct1 = {1:'qwweert', 2:00000, 3:3, 5:'rrrrr', 'ddd':5};
var dct2 = {1:1, 2:45, 'ddd':3, 8:5677, 5:5789};
var tt  = counttyp([112345,[1,4,6], 'test', 3, [], {}, 0.789, 'ssss'] );
ttt = eq_key(dct1, dct2);
var t = types_of_args(1, 's', 2, 'ssss', 2.4, [5,6,7,8], {}, []);

console.log(tt);
console.log('В словарях общих ключей %d.', ttt );
console.log('Типы  аргументов', t)

pMatr([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11,1]]);
List_of_list([[3, 0, 1], [4, 0, 9], [9, 0, 9]]);
