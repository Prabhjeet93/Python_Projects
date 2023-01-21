// This java script code will update the github repositories history.


const jsonfile = require('jsonfile');

const moment = require('moment');

const simpleGit = require("simple-git")

const FILE_PATH = './data.json';

const DATE = moment().subtract(85,'d').format();

const data = {
    date: DATE
}

jsonfile.writeFile(FILE_PATH, data);

simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE }).push();

//########################################################################################################

const jsonfile = require('jsonfile');

const moment = require('moment');

const simpleGit = require("simple-git")

const FILE_PATH1 = './data.json';

const DATE1 = moment().subtract(3,'d').format();

const data1 = {
    date: DATE
}

jsonfile.writeFile(FILE_PATH1, data, ()=> {
    simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE }).push();
});


// #############################################################################################################

const jsonfile = require('jsonfile');

const moment = require('moment');

const simpleGit = require("simple-git")

const FILE_PATH2 = './data.json';

const makeCommit2 = (x,y) => {
    const DATE = moment().subtract(1,'y').add(1,'d').add(x,'w').add(y,'d').format();

    const data = {
    date: DATE
    }

    jsonfile.writeFile(FILE_PATH, data, ()=> {
    simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE }).push();
    });

}

makeCommit2(3,3)

//##############################################################################################################3

const jsonfile = require('jsonfile');
const moment = require('moment');
const simpleGit = require("simple-git");
//const random = require('random');
//`import random from 'random'`


const FILE_PATH3 = './data.json';

const makeCommit = n => {
    if(n===0) return simpleGit().push();
    const x = Math.random()*100;
    const y = Math.random()*100;
    const DATE = moment().subtract(1,'y').add(1,'d').add(x,'w').add(y,'d').format();

    const data = {
    date: DATE
    }
    console.log(DATE);
    jsonfile.writeFile(FILE_PATH, data, ()=> {
    simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE },
    makeCommit.bind(this, --n));
    });

}

makeCommit(50);