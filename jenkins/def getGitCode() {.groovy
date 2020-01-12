def getGitCode() {
	git branch: params.gitBranch, credentialsId: 'myCred', url: 'git@github.com:evgeniyv6/django_sample.git'
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
  try {
    timestamps {
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