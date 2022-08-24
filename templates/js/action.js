import {render_Line_Chart, render_table} from "/js/render/render.js";

let datalist = [{ "quoted_date": "2022/08/24", "currency": "USA", "cash_buying": 29.8, "cash_selling": 30.47, "spot_buying": 30.15, "spot_selling": 30.25 }, 
                { "quoted_date": "2022/08/23", "currency": "USA", "cash_buying": 29.805, "cash_selling": 30.475, "spot_buying": 30.155, "spot_selling": 30.255 }, 
                { "quoted_date": "2022/08/22", "currency": "USA", "cash_buying": 29.7, "cash_selling": 30.37, "spot_buying": 30.05, "spot_selling": 30.15 }, 
                { "quoted_date": "2022/08/19", "currency": "USA", "cash_buying": 29.625, "cash_selling": 30.295, "spot_buying": 29.975, "spot_selling": 30.075 }, 
                { "quoted_date": "2022/08/18", "currency": "USA", "cash_buying": 29.6, "cash_selling": 30.27, "spot_buying": 29.95, "spot_selling": 30.05 },
                { "quoted_date": "2022/08/17", "currency": "USA", "cash_buying": 29.585, "cash_selling": 30.255, "spot_buying": 29.935, "spot_selling": 30.035 }, 
                { "quoted_date": "2022/08/16", "currency": "USA", "cash_buying": 29.6, "cash_selling": 30.27, "spot_buying": 29.95, "spot_selling": 30.05 }, 
                { "quoted_date": "2022/08/15", "currency": "USA", "cash_buying": 29.59, "cash_selling": 30.26, "spot_buying": 29.94, "spot_selling": 30.04 }, 
                { "quoted_date": "2022/08/12", "currency": "USA", "cash_buying": 29.575, "cash_selling": 30.245, "spot_buying": 29.925, "spot_selling": 30.025 }]

let xTarget = d => new Date(d.quoted_date)
let yTarget = d => d.cash_selling
let targetList = datalist.map(obj => obj.cash_selling)
let yAvg = targetList.reduce((pre, cur) => pre + cur, 0) / targetList.length
let yMax = Math.max(...targetList)
let yMin = Math.min(...targetList)
let sigma = Math.sqrt((targetList.reduce((pre, cur) => pre + Math.pow(cur, 2), 0) / targetList.length) - Math.pow(yAvg, 2))
let label =  "↑ Cash Selling ($)"

let setting = {
    x: xTarget,
    y: yTarget,
    yDomain: [yMin - sigma, yMax + sigma],
    yLabel: label,
    color: "steelblue"
}

render_Line_Chart(datalist, setting, document.querySelector(".content"))

let obj1 = {
    "currency": "USA",
    "cash_buying": 30.5,
    "cash_selling": 29.5,
    "spot_buying": 30,
    "spot_selling": 29
}

let obj2 = {
    "currency": "JP",
    "cash_buying": 3,
    "cash_selling": 2,
    "spot_buying": 3,
    "spot_selling": 2
}

const renderTarget = document.querySelector(".content");
let input_json = [obj1, obj2]

document.querySelector("#test-click").onclick = () => {
    render_table(input_json, document.querySelector(".content"));
}
