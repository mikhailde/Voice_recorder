function getPathToFile() {
   eel.pythonFunction()(r =>
      {if (r === 'true') {
         alert('Файл был успешно загружен')
       } else {
         console.log(r)
         alert('Допустимы только файлы .csv')
       }
      }
      )
   };