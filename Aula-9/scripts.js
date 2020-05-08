let data;
let count = 0;
let playerAction;
let jogadaDoBot = [];

function getInfo(){

    data = {
        Nome: "",
        Idade: "",
        Altura: "",
        RA: ""
    }

    Object.entries(data).forEach(([prop, value], index) => {
        data[`${prop}`] = prompt("Digite o(a)" + prop + ":");
        count++;
    });

    return data;
}

function showInfo(){
    let returnedData;
    returnedData = getInfo();

    if( count == Object.keys(returnedData).length)
        alert("Mostrando os dados digitados:\n"+
        "Nome: "+returnedData.Nome+"\n"+
        "Idade: "+returnedData.Idade+"\n"+
        "Altura: "+returnedData.Altura+"\n"+
        "RA: "+returnedData.RA+"\n");
}

function rngInator(){
    switch(Math.floor((Math.random() * 3 ) + 1)){
        case 1:
            return "tesoura";
        case 2:
            return "papel";
        case 3:
            return "pedra";
    }
}

function oJogo(){
    //let playerAction = [];
    let jogadasDoPlayer = {
        vitorias: 0,
        derrotas: 0,
        empates: 0,
        jogadas: []
    };

    let jogadasDoBot = {
        vitorias: 0,
        derrotas: 0,
        empates: 0,
        jogadas: []
    };

    playerAction = prompt("Digite as suas jogadas:");
    
    playerAction = playerAction.split(", ");
    jogadaDoBot = [];
    let contadorjogadaDoBot = 0;
    for(let i = 0; i < playerAction.length; i++) {
        jogadaDoBot[i] = rngInator();
        
        jogadasDoPlayer.jogadas = playerAction;
        jogadasDoBot.jogadas += jogadaDoBot[i];
        if( i + 1 > playerAction.length || i + 1 === playerAction.length)
            jogadasDoBot.jogadas += " " ;
        else jogadasDoBot.jogadas += ", ";

        if(playerAction[i] ===  jogadaDoBot[i]){
            jogadasDoPlayer.empates++;
            jogadasDoBot.empates++;
        } else if( playerAction[i] !== jogadaDoBot[i]) {
            if(playerAction[i].length > jogadaDoBot[i].length){
                if(jogadaDoBot[i] === "papel") {
                    jogadasDoPlayer.vitorias++;
                    jogadasDoBot.derrotas++;
                } else if(jogadaDoBot[i] === "pedra") {
                    jogadasDoPlayer.derrotas++;
                    jogadasDoBot.vitorias++;
                }
            } else if (playerAction[i].length < jogadaDoBot[i].length) {
                if(playerAction[i] === "papel") {
                    jogadasDoPlayer.derrotas++;
                    jogadasDoBot.vitorias++;
                } else if(playerAction[i] === "pedra") {
                    jogadasDoPlayer.vitorias++;
                    jogadasDoBot.derrotas++;
                }
            }
            else if(playerAction[i] === "pedra" && jogadaDoBot[i] === "papel") {
                jogadasDoPlayer.derrotas++;
                jogadasDoBot.vitorias++;
            } else if (playerAction[i] === "papel" && jogadaDoBot[i] === "pedra") {
                jogadasDoPlayer.vitorias++;
                jogadasDoBot.derrotas++;
            }
        }
        contadorjogadaDoBot++;
        console.log(jogadasDoBot.jogadas);
        console.log(contadorjogadaDoBot);
    }

    alert("Os resultados foram:\n\n"+
    "Jogador:\n"+
    "vitorias:"+jogadasDoPlayer.vitorias+"\n"+
    "derrotas:"+jogadasDoPlayer.derrotas+"\n"+
    "empates:"+jogadasDoPlayer.empates+"\n"+
    "jogadas:"+jogadasDoPlayer.jogadas+"\n"+
    "\nBot:\n"+
    "vitorias:"+jogadasDoBot.vitorias+"\n"+
    "derrotas:"+jogadasDoBot.derrotas+"\n"+
    "empates:"+jogadasDoBot.empates+"\n"+
    "jogadas:"+jogadasDoBot.jogadas+"\n");
}

showInfo();
oJogo();