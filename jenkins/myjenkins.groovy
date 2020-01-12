def getGitCode() {
	git branch: params.gitBranch, credentialsId: 'myCred2', url: 'ssh://git@bitbucket.org:company/repo.git'
}

def ansiblePlaybook() {
  ansiColor('xterm') {
    ansiblePlaybook(
        colorizes: true,
        inventory: './ansible/inventory',
        playbook: './ansible/site.yml',
        disableHostKeyChecking: true,
      )
  }
}

node('master') {
  timestamps {
  try {
    stage('Getting GIT') {
      println("get code in to the ${WORKSPACE}")
      getGitCode()
    }
    stage('Run ansible playbook') {
      ansiblePlaybook()
    }
  } catch (Exception err) {
    println("We catch the error: ${err}")
  } finally {
    cleanWs()
    }
  }
}