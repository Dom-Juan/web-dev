let numeroDeFilhos = 20;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function AdicionaConteudo(){
    i = 0;
    
    while(i < numeroDeFilhos) {
        await sleep(1000);
        document.getElementById('coisas').innerHTML+=`<div class='postBox'><textarea class="postBox" name="text" rows="5" cols="33">Texto</textarea></div>`;
        i++;
    }
}