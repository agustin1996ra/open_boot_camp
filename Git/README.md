# Git

## Comandos

### Configuración Básica

Configurar Nombre que salen en los commits

```bash
git config --global user.name "dasdo"
```

Configurar Email

```bash
git config --global user.email dasdo1@gmail.com
```

Marco de colores para los comando

```bash
git config --global color.ui true
```

### Iniciando repositorio

Iniciamos GIT en la carpeta donde esta el proyecto

```bash
git init
```

Clonamos el repositorio de github o bitbucket

```bash
git clone <url>
```

Añadimos todos los archivos para el commit

```bash
git add .
```

Hacemos el primer commit

```bash
git commit -m "Texto que identifique por que se hizo el commit"
```

subimos al repositorio

```bash
git push origin master
```

### GIT CLONE

Clonamos el repositorio de github o bitbucket

```bash
git clone <url>
```

Clonamos el repositorio de github o bitbucket ?????

```bash
git clone <url> git-demo
```

### GIT ADD

Añadimos todos los archivos para el commit

```bash
git add .
```

Añadimos el archivo para el commit

```bash
git add <archivo>
```

Añadimos todos los archivos para el commit omitiendo los nuevos

```bash
git add --all 
```

Añadimos todos los archivos con la extensión especificada

```bash
git add *.txt
```

Añadimos todos los archivos dentro de un directorio y de una extensión especifica

```bash
git add docs/*.txt
```

Añadimos todos los archivos dentro de un directorios

```bash
git add docs/
```

### GIT COMMIT

Cargar en el HEAD los cambios realizados

```bash
git commit -m "Texto que identifique por que se hizo el commit"
```

Agregar y Cargar en el HEAD los cambios realizados

```bash
git commit -a -m "Texto que identifique por que se hizo el commit"
```

De haber conflictos los muestra

```bash
git commit -a 
```

Agregar al ultimo commit, este no se muestra como un nuevo commit en los logs. Se puede especificar un nuevo mensaje

```bash
git commit --amend -m "Texto que identifique por que se hizo el commit"
```

### GIT PUSH

Subimos al repositorio

```bash
git push <origien> <branch>
```

Subimos un tag

```bash
git push --tags
```

### GIT LOG

Muestra los logs de los commits

```bash
git log
```

Muestras los cambios en los commits

```bash
git log --oneline --stat
```

Muestra graficos de los commits

```bash
git log --oneline --graph
```

### GIT DIFF

Muestra los cambios realizados a un archivo

```bash
git diff
git diff --staged
```

### GIT HEAD

Saca un archivo del commit

```bash
git reset HEAD <archivo>
```

Devuelve el ultimo commit que se hizo y pone los cambios en staging

```bash
git reset --soft HEAD^
```

Devuelve el ultimo commit y todos los cambios

```bash
git reset --hard HEAD^
```

Devuelve los 2 ultimo commit y todos los cambios

```bash
git reset --hard HEAD^^
```

Rollback merge/commit

```bash
git log
git reset --hard <commit_sha>
```

### GIT REMOTE

Agregar repositorio remoto

```bash
git remote add origin <url>
```

Cambiar de remote

```bash
git remote set-url origin <url>
```

Remover repositorio

```bash
git remote rm <name/origin>
```

Muestra lista repositorios

```bash
git remote -v
```

Muestra los branches remotos

```bash
git remote show origin
```

Limpiar todos los branches eliminados

```bash
git remote prune origin 
```

### GIT BRANCH

Crea un branch

```bash
git branch <nameBranch>
```

Lista los branches

```bash
git branch
```

Comando -d elimina el branch y lo une al master

```bash
git branch -d <nameBranch>
```

Elimina sin preguntar

```bash
git branch -D <nameBranch>
```

### GIT TAG

Muestra una lista de todos los tags

```bash
git tag
```

Crea un nuevo tags

```bash
git tag -a <verison> - m "esta es la versión x"
```

### GIT REBASE

Los rebase se usan cuando trabajamos con branches esto hace que los branches se pongan al día con el master sin afectar al mismo

Une el branch actual con el master, esto no se puede ver como un merge

```bash
git rebase
```

Cuando se produce un conflicto no das las siguientes opciones:

cuando resolvemos los conflictos --continue continua la secuencia del rebase donde se pauso

```bash
git rebase --continue 
```

Omite el conflicto y sigue su camino

```bash
git rebase --skip
```

Devuelve todo al principio del rebase

```bash
git reabse --abort
```

Para hacer un rebase a un branch en especifico

```bash
git rebase <nameBranch>
```

### OTROS COMANDOS

Lista un estado actual del repositorio con lista de archivos modificados o agregados

```bash
git status
```

Quita del HEAD un archivo y le pone el estado de no trabajado

```bash
git checkout -- <file>
```

Crea un branch en base a uno online

```bash
git checkout -b newlocalbranchname origin/branch-name
```

Busca los cambios nuevos y actualiza el repositorio

```bash
git pull origin <nameBranch>
```

Cambiar de branch

```bash
git checkout <nameBranch/tagname>
```

Une el branch actual con el especificado

```bash
git merge <nameBranch>
```

Verifica cambios en el repositorio online con el local

```bash
git fetch
```

Borrar un archivo del repositorio

```bash
git rm <archivo> 
```

### Fork

Descargar remote de un fork

```bash
git remote add upstream <url>
```

Merge con master de un fork

```bash
git fetch upstream
git merge upstream/master
```

### GIT BISECT

## Introducción al control de versiones

### Sistemas de control de versiones

Hay tres tipos de controles de versiones, los locales, los centralizados y los distribuidos.

#### Sistemas de control de versiones local

El primer sistema de control de versiones de archivos fue "rcs". Es una una solución solamente local, y soluciona el tema de versiones, pero no ofrece ninguna forma de compartir el repositorio con alguien mas.

#### Sistemas de control de versiones centralizado

Uno de los que se sigue utilizando en este tipo de software de control de versiones es la evolución de RCS, llamada CVS. Otro de los sistemas utilizados es SUBVERSION (SVN). Estos sistemas si bien se siguen utilizando, pero es raro encontrárselos.

Estos sistemas utilizan servidores para guardar nuestros repositorios.

La siguiente evolución de estos es git.

#### Sistemas de control de versiones distribuidos

Esta es la tercera generación de sistemas de controles de versiones.

El líder de esta generación es GIT, pero no es el único. Hay otros que compitieron con git por un tiempo, estos son mercurial y bazaar. Estos se siguen usando, pero son mucho menos populares que GIT.

La ventaja que trae esta generación, es que trabajan tanto de forma local como con un servidor. Esto significa que podemos hacer cambios en nuestro repositorio, y una vez que tengamos conexión a internet, enviar los cambios a el repositorio remoto en un servidor.

### Primer repositorio en git

Creo un repositorio, primero creando un carpeta, y luego desde la consola, ingreso en la carpeta y con el comando `git init .`, inicializamos el repositorio. Este comando creara archivos para la gestión de versiones.

Para empezar hemos creado un archivo y lo hemos confinado, luego le hemos realizado un cambio que también lo hemos confirmado. Para ello hemos usado el comando `echo` para crear un archivo y pasarle un texto de contenido, con la siguiente sintaxis: `echo Hola > mensaje`. Siendo la palabra "hola" el texto que hemos agregado y mensaje el nombre del archivo. Luego para confirmar el archivo en nuestro repositorio usamos el comando `git add mensaje` y después `git commit -m "Mensaje inicial"`. `git add` agregara a al area de preparación el archivo o carpeta especificado y el comando `git commit -m "titulo del commit"` aceptara todos los cambios agregados al area de preparación. Estos commits o confirmaciones generaran un historial.

El historial podrá ser consultado usando el comando `git log` el cual mostrara todos los commits del repositorio, cada commit tendrá metadatos, como la fecha de confirmación, el hash, el autor y el titulo o descripción.

Todos estos cambios confirmados esta alojados de forma local, podríamos vincular este repositorio con uno remoto y empujar estos cambios a este.

```bash
rodri@laptop-agus MINGW64 /c/rep/practica_git_obc (main)
$ git log
commit 4c941077bfe0e29ff0ddf1a1ed573ba566f4fe24 (HEAD -> main)
Author: agustin1996ra <rodriguezalvarezagustin@gmail.com>
Date:   Wed Jul 12 18:31:27 2023 -0300

    cambios al mensaje

commit b7c64fd429c7ee7e72c1ff3eaadcf79b12537ee9
Author: agustin1996ra <rodriguezalvarezagustin@gmail.com>
Date:   Wed Jul 12 18:29:57 2023 -0300

    Mensaje inicial

```

Lo que vemos a continuación es todos los archivos alojados en la carpeta .git, que se crea al iniciar nuestro repositorio

```bash
rodri@laptop-agus MINGW64 /c/rep/practica_git_obc/.git (GIT_DIR!)
$ ls -altr
total 17
-rw-r--r-- 1 rodri 197609  73 jul. 12 18:27 description
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:27 hooks/
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:27 refs/
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:27 info/
-rw-r--r-- 1 rodri 197609  21 jul. 12 18:27 HEAD
-rw-r--r-- 1 rodri 197609 130 jul. 12 18:27 config
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:27 ../
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:29 logs/
-rw-r--r-- 1 rodri 197609 137 jul. 12 18:31 index
-rw-r--r-- 1 rodri 197609  19 jul. 12 18:31 COMMIT_EDITMSG
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:31 ./
drwxr-xr-x 1 rodri 197609   0 jul. 12 18:31 objects/
```

Si usamos el comando `find .` también veremos las sub carpetas y todos los archivos. Si prestamos atencion a la carpeta objects, veremos hashes donde se guardar nuestro codigo fuente, de igual manera no podremos leer ni entender estos archivos, ya que estan comprimidos.

```bash
rodri@laptop-agus MINGW64 /c/rep/practica_git_obc/.git (GIT_DIR!)
$ find .
.
./COMMIT_EDITMSG
./config
./description
./HEAD
./hooks
./hooks/applypatch-msg.sample
./hooks/commit-msg.sample
./hooks/fsmonitor-watchman.sample
./hooks/post-update.sample
./hooks/pre-applypatch.sample
./hooks/pre-commit.sample
./hooks/pre-merge-commit.sample
./hooks/pre-push.sample
./hooks/pre-rebase.sample
./hooks/pre-receive.sample
./hooks/prepare-commit-msg.sample
./hooks/push-to-checkout.sample
./hooks/update.sample
./index
./info
./info/exclude
./logs
./logs/HEAD
./logs/refs
./logs/refs/heads
./logs/refs/heads/main
./objects
./objects/19
./objects/19/c70a3e67953361e0cb365291fee552a4872e6c
./objects/35
./objects/35/86f9d724655582e3c3edde85e040186fa69b38
./objects/4c
./objects/4c/941077bfe0e29ff0ddf1a1ed573ba566f4fe24
./objects/5c
./objects/5c/1b14949828006ed75a3e8858957f86a2f7e2eb
./objects/b7
./objects/b7/c64fd429c7ee7e72c1ff3eaadcf79b12537ee9
./objects/dc
./objects/dc/ab3afdb79acbe69b1fbc296e2fe517f3a40b29
./objects/info
./objects/pack
./refs
./refs/heads
./refs/heads/main
./refs/tags
```

### Servicios de repositorios remotos

A la hora de queres trabajar en equipo y compartir nuestro codigo, siempre podriamos compartir un archivo comprimido de nuestro repositorio, pero esto es bastante ineficiente. Lo mejor que podemos hacer es trabajar con un servidor. Tenemos la posibilidad de crear nuestro propio repositorio o de utilizar uno de los servidores de empresas dedicadas a esto.

Esta empresas que proveen servidores para nuestros repositorios son:

- GitHub
- GitLab
- Bitbucket
- SourceForge

Estas cuatro son las mas utilizadas, ordenadas por importancia en el sector. Después de la compra de GitHub por parte de microsoft, muchos usuarios se han mudado a GitLab.

En un lejano y tercer lugar se encuentra Bitbucket, la cual su comunidad suele estar vinculada con el desarrollo en Java, y es parte de las soluciones de la empresa que desarrollo Jira.

Y por ultimo, "el rey destronado" SourceForge, quien es su momento fue el mas utilizado, ya ahora prácticamente en desuso. Pero ofrece unas características que los otros no, ya que permite guardar repositorios mercurial y subversion.

### Publicar un repositorio en GitHub

Debemos tener una cuenta de GitHub, luego creamos un repositorio, y podemos agregar la dirección de nuestro repositorio remoto a nuestro local, para que cuando ejecutemos el comando `git push` los cambios confirmados se suban.

Para agregar una dirección de repositorio remoto debemos utilizar el comando `git remote add origin https://github.com/usuario/nombre-repo.git`.

> La palabra origin siempre hará referencia a el remoto.
> Para poder publicar una rama que no existe en el remoto debemos utilizar el comando `git push -u origin nombre-rama`, en el caso de ser un repositorio nuevo deberemos hacerlo con la rama main.

## Instalación

## Nuestro propio servidor para repositorios

Esto lo haremos con gitea. Primer requisito para usar gitea es tener instalado Docker.

Para buscar el instalador de gitea, vamos a recurrir a DockerFile, que es una pagina, donde se suben las imágenes de varios sistemas, ya personalizados, para diferentes tareas.

Para crear un conteiner de gitea escribiremos un archivo `docker-compose.yml`, dentro de una carpeta llamada gitea. Luego ejecutaremos el comando `docker-compose up`.

```yml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:1.20
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    nerworks:
      - gitea
    volumes:
      - ./gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
```

## Repositorio local I

En esta clase, vamos a trabajar en un repositorio local.

Vamos a crear una carpeta llamada `miapp`, y vamos a agregar archivos y ficheros como si fuesen las partes de un proyecto.

Con el comando `git init` dentro de la carpeta `miapp` vamos a transformar esta carpeta en un repositorio git. Luego vamos a almacenar los cambios en el `staging area`, ahora estos cambios no estan confirmados. Para confirmarlos en el repositorio debemos usar el comando `git commit`.
Antes de confirmarlo vamos a hacer una configuraciones en el repositorio.

### Configuraciones de git

Esta esta partida en tres partes, `system` es la que esta a traves de todo el sistema (raramente utilizada), tenemos también `global` que es la que influye en e todos los repositorios de mi usuario y `local` la cual solo influye en la configuración de mi repositorio actual.

Para hacer cambios en estas tres vamos a usar el comando `git config` seguido por el tipo de configuración que vamos a realizar. Por ejemplo:
    - `git config --system`
    - `git config --global`
    - `git config --local`

A tener en cuenta que la jerarquía de las configuraciones esta dada por cual esta mas cerca del repositorio, por ejemplo las configuraciones globales sobreescriben las de sistema, como las configuraciones locales del repositorio sobreescriben las configuraciones globales del usuario.

Para poder ver la configuración actual, podemos usar el comando `git config --list` seguido del nivel que deseamos ver de configuración ya sea `--system`, `--global` o `--local`.

Cuando editamos configuraciones con el comando `git config --local` estamos editando el archivo `.git/config` de nuestro repositorio. Cuando editamos las configuraciones globales estamos editando el fichero `$HOME/.gitconfig`. Y cuando lo hacemos con el comando `git config --system` estoy modificando el archivo `/etc/gitconfig`

#### Cambiar una configuración

Para cambiar una configuración vamos a usar principalmente global o local.

Por ejemplo para cambiar el usuario:  `git config --global user.name "Nombre de Usuario"`

Por ejemplo para cambiar el mail para el repositorio: `git config --local user.mail "Mail de trabajo"`. Esta configuración solo tendrá efecto en el uso del repositorio, fuera de este tendré efecto la configuración que tenga en el archivo global de configuración.

Este tipo de configuraciones es importante tenerlas encuentra para cuando vamos a usar repositorios públicos, ya que si uno desea que la información personal de las direcciones email o de nuestro nombre completo, es la única opción configurar para estos repositorios en particular usuarios y mail que no sean nuestros principales. En el caso de usar github, este servicio nos provee de direcciones email que no revelan nuestros datos.

Por ejemplo al realizar un `git log` veremos los datos que tenemos configurados, en mi caso en `global`, si yo quisiera publicar este repositorio y que mis datos no queden publicos lo que debo hacer es configurar el repositorio de manera `local` indicando unos datos que resguarden mi privacidad.

```bash
rodri@laptop-agus MINGW64 /c/rep/miapp (main)
$ git log
commit bc2c4004aea808f4f7d58ee8b72c202f3ce43c3e (HEAD -> main)
Author: agustin1996ra <rodriguezalvarezagustin@gmail.com>
Date:   Thu Jul 20 18:54:09 2023 -0300

    Cambio el texto de LICENSE

commit f151eed0b24765921f8c20b754cf3c95112b7c96
Author: agustin1996ra <rodriguezalvarezagustin@gmail.com>
Date:   Thu Jul 20 18:52:56 2023 -0300

    primera confirmacion
```

### Otra forma de iniciar un repositorio

Podemos crear un repositorio también con el siguiente comando `git init --bare aplicacion`, en el cual indicamos el nombre de la carpeta de repositorio al final. Este comando lo que quiere decir es que crearemos un repositorio en un lugar, pero trabajaremos en otro lado. Osea el registro de cambios se guardara en otro lugar de donde tenemos nuestros archivos. PAra usar este repositorio una vez creado tengo que usar un `git clone` y la dirección de el repositorio "remoto".

## Git Sesión 4

- `git bisect`: Este comando se utiliza empezando con un `git bisect start`, luego se le pasa el ultimo commit "bueno" donde nuestro proyecto funcionaba con el comando `git bisect good <hash>`. Y después le pasaremos el hash del commit donde dejo de funcionar con el comando `git bisect bad <hash>`.

- `git blame <ruta archivo>` nos permite ver que usuarios y cuando alteraron un archivo

