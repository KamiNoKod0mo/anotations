# anotations
Some example codes for me to remember

git init
git status
git add .
git commit -m 'initial commit'
git log
git checkout ...
git diff
git log -p -x --stat
git log -- file.txt
git log  --graph
git log --oneline --author=""
git log grep="Olá"

git checkout -b aulaBranch
git branch     ,-v
git merge

git config -l --local/remote
git config --local alias.st 'status'
git config --unset alias.st

git commit --amend --no-edit
Co-authored-by: carlos <carlos.gmail.com>
 git rebase -i HEAD~5
squash junta commits pequenos
edit mudar o commit e o arquivo

git tag -a v1.0 -m "mensagem"   //usar no git checkout
git show --tags
git tag -n
git tag -d v1.0


git remote set-url origin ...
git remote add local ...       #sistema de backup
    git init -bare , dps adcionar no repositior em funcionameto
    git clone , git fetch origin main:main

git remote remove ... 
git pull orgin master      {fetch,merge}
git push origin master
git fetch origin master                 #Não incorpora
git diff master origin/main
git push --tag     (para criar releases no github) podendo fazer um draft

commit template
issues #1, pode ser referenciado na msg do commit

#--------
> Estudo sobre
> Estudo
*item 1
*item 2

Ir para pgatina do [google](https://www.google.com)
![imagem]()
<img src="..." width=500>

- [ ] Lista
- [ ] Lista

```c
int main(void){
    printf("Ola\n");
}
```

column 1 | column 2 | column 3 |
---|---|---|
AAAA | BBBB | CCCC |
12 | 13 | 14 |

Hospedagem
Nome repositorio arquivo.github.io

Wiki

