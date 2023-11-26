<# echo "teste"
Write-Host "teste2"
Write-Output 'Teste 3'

Write-Host "$(ls)"
"$(Get-Location)"

$var = Read-Host "Algo: "
echo "$var"
Write-Host "$(ls)" | Select-String "webx"
#>
#-gt,-ge ...
param($p1,$port)#argumentos
function pingswep {
    param (
        [string]$teste
    )
    if (!$teste){
        echo "Script ping"
        echo "Modo de uso: .\anonPwP.ps1 192.168.0"
    }else {
        foreach ($ip in 1..254) {
            try {
                $var = ping -n 1 "$teste.$ip" | Select-String "ttl=64" 
                $var.Line.split(' ')[2] -replace ":",""
            }catch {
                
            }
        }
    
    }
}

function portscan {
    param (
        [string]$ip,
        [string]$port
    )
    if (!$ip -or !$port){
        echo "Script ping"
        echo "Modo de uso: .\anonPwP.ps1 192.168.0.1 80"
    }else {
        #-traceroute
        #-Hop
        if (Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet) {
            echo "Porta Aberta"
        } else {
            echo "Porta Fechada"
        }
    }
}

function web{
    param (
        [string]$site
    )
    $si = Invoke-WebRequest -uri "$site" -Method GET -UseBasicParsing
    #-OutFile x.txt

    #$si.headers
    #.statuscode
    #.content
    $si.links.href | Select-String http://
    
    
    
}

#pingswep -teste $p1
#portscan -ip $p1 -port $port
#web -site "http://www.google.com"

#Get-Command | Select-String Test
#Get-Help




