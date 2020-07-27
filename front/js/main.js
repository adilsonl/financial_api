function get_ibovespa(){
    $.ajax({
        url:'http://127.0.0.1:5000/ibovespa',
        type:"GET",
        success:function(response){
            console.log(response)
            $('#nameCompany').html("Ibovespa")
            $('#pointsCompany').html("Pontos: "+response.points)

        }
    })
}
function get_company_points(symbol,company){
    $.ajax({
        url:`http://127.0.0.1:5000/points/${symbol}`,
        type:"GET",
        success:function(response){
            console.log(response)
            $('#nameCompany').html(company)
            if(response.points !== undefined)
                $('#pointsCompany').html("Pontos: "+response.points)
            else
                 $('#pointsCompany').html("Erro ao carregar aos pontos")

        }
    })
}

function serachCompanies(){
    var company = document.getElementById('searchCompany').value;
    clearResults()
    $.ajax({
        url:`https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${company}&apikey=NW84PZQEPS9SN9S7`,
        type:"GET",
        success:function(response){
            console.log(response)
            var bestMatches = response.bestMatches;
            if(bestMatches.length > 0){
                for(match of bestMatches){
                    var functionButton = `get_company_points("${match['1. symbol']}","${match['2. name']}")`
                    var $button = $(`<button type="button" class="btn btn-secondary" onclick='${functionButton}'>${match['2. name']}</button>`)
                    $button.appendTo($("#results"));
                }
            }else{
                var $text = $('<br><h2 id="warning">Sem resultados</h2>');
                $text.appendTo($("#results"));
            }
        }
    })
}

function clearResults(){
    $("#results").empty()
}