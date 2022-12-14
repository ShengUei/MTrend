import { LineChart } from "/js/D3/lines/lineChart.js";
import { MutipleLineChart } from "/js/D3/lines/mutipleLineChart.js";
import { CandlestickChart } from "/js/D3/lines/candlestickChart.js";

//建立 <table></table>
//@input: input_json 物件陣列
//@input: renderTarget 要建立的 element 位子
export function render_table(input_json, renderTarget) {
    //先清空 renderTarget 的內容
    renderTarget.innerHTML = "";

    let docFrag = document.createDocumentFragment();
    let table = document.createElement("table");    
    let thead = document.createElement("thead");    
    let tbody = document.createElement("tbody");
    let tr;
    let th;
    let td;

    //建立 thead 並插入值
    tr = document.createElement("tr");

    for(let propertyName in input_json[0]) {
        th = document.createElement("th");
        th.innerHTML = propertyName;
        tr.appendChild(th);
    }

    thead.appendChild(tr);
    table.appendChild(thead);
    
    //建立 tbody 並插入值
    for(let obj of input_json) {
        tr = document.createElement("tr");

        for(let propertyName in obj) {
            td = document.createElement("td");
            td.innerHTML = obj[propertyName];
            tr.appendChild(td);
        }

        tbody.appendChild(tr);
    }
    
    table.appendChild(tbody);
    docFrag.appendChild(table);
    renderTarget.appendChild(docFrag);
}

export function render_Line_Chart(input_json, setting, renderTarget) {
    //先清空 renderTarget 的內容
    renderTarget.innerHTML = "";

    let chart = LineChart(input_json, setting)

    renderTarget.appendChild(chart);
}

export function render_Mutiple_Line_Chart(input_json, setting, renderTarget) {
    //先清空 renderTarget 的內容
    renderTarget.innerHTML = "";

    let chart = MutipleLineChart(input_json, setting)

    renderTarget.appendChild(chart);
}

export function render_Candlestick_Chart(input_json, setting, renderTarget) {
    //先清空 renderTarget 的內容
    renderTarget.innerHTML = "";

    let chart = CandlestickChart(input_json, setting)

    renderTarget.appendChild(chart);
}
