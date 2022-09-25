//program downlode file with promise  and await

const url1 = "file1/this com/SA"
const url2 = "file2/this com/SA"
const url3 = "file3/this com/SA"
const url4 = "file4/this com/SA"


const connect = true 
function Downlode(url) {
    return new Promise(function(resolve,reject) {
        console.log("Downloding...",url)
        setTimeout(()=>{
            if(connect){
                resolve("Downlode finited")
            }else{
                reject("error")
            }
        },1500)
        
    })
}


async function start() {
    console.log(await Downlode(url1))
    console.log(await Downlode(url2))
    console.log(await Downlode(url3))
    console.log(await Downlode(url4))
}

start()