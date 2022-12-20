let id = 1
let max_id = 0
let log = []
let cnt = -1
let check = false
let sum = 0
function next_text() {

    if (check === false){
      log = [`ID: ${id}`,'Статус: пропущено', `Количество попыток: ${+cnt+1}`]
      eel.write_log(log)
    } else {sum += 1}
    progress = document.getElementById('progress')
    progress.innerHTML = `${sum}/${max_id}`
    cnt = -1
    check = false
    
    document.getElementById(`${id}`).classList.remove("u-active")
    id ++
    if (id === +max_id + 1){id = 1}
    document.getElementById(`${id}`).classList.add("u-active")

}
function prev_text() {
    cnt = -1
    check = false
    document.getElementById(`${id}`).classList.remove("u-active")
    id -= 1
    if (id === 0){id = max_id}
    document.getElementById(`${id}`).classList.add("u-active")
}
function getPathToFile() {
    eel.upload_file()(r =>
       {if (r === 'true') {
          alert('Файл был успешно загружен')
          let carousel = document.getElementById("carousel")
          
          eel.parser()(res => {
             for (key in res){
                let div1 = document.createElement('div');
                div1.setAttribute('id',`${key}`)
                div1.setAttribute('class',`u-align-center u-carousel-item u-container-style u-gradient u-slide u-carousel-item-${key}`)
                if (key === '1') {div1.classList.add("u-active")}
                let div2 = document.createElement('div')
                div2.setAttribute('class',`u-container-layout u-container-layout-${key}`)
                h4 = document.createElement('h4')
                h4.setAttribute('class',`u-align-center u-custom-font u-font-ubuntu u-text u-text-palette-2-base u-text-${key}`)
                h4.innerText = `Текст ${key}`
                p = document.createElement('p')
                p.setAttribute("class",`u-align-center u-small-text u-text u-text-variant u-text-${key}`)
                p.setAttribute("style","height:300px; font-size:16px; overflow-y: scroll;")
                p.innerText = res[key][0]
                ins=document.createElement('p')
               //  ins.setAttribute("hidden")
                ins.innerText = res[key][1]
                div2.appendChild(h4)
                div2.appendChild(p)
                div2.appendChild(ins)
                div1.appendChild(div2)
                carousel.appendChild(div1)

                max_id = key
             }
          })
        } else {
          alert('Допустимы только файлы .csv')
        }
       }
       )
    };
let flag = 0
function record() {
   if (flag === 0){
   flag = 1;
   document.getElementById('recording').innerHTML = '<span class="u-file-icon u-icon u-text-palette-2-base u-icon-3"><img src="images/4015830-4d71bb22.png" alt=""></span>&nbsp;стоп<br>';
   console.log('ok');
   eel.recording();
   } else {
      cnt += 1
      flag = 0
      document.getElementById('recording').innerHTML = '<span class="u-file-icon u-icon u-text-palette-2-base u-icon-3"><img src="images/4015830-4d71bb22.png" alt=""></span>&nbsp;запись<br>';
      eel.recording();
   }
}

function save(){
   check = true
   log = [`ID: ${id}`,'Статус: записано', `Количество попыток: ${+cnt+1}`]
   cnt = -1
   eel.write_log(log)
   eel.save_file(id)(r => {
      if (r === 'true')
         {alert('Файл был успешно сохранен')
      } else {
         alert('Неверно выбрана директория')  
      }
   })
}

function listen(){
   eel.listener()
}


