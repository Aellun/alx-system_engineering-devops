## Project Name: 0x17. Web stack debugging #3

# Project description

    In this project we are looking into the following concepts
        Web Server
        Web stack debugging

Apache is the web server we want to debug

# Technologies installed:
    puppet-lint -v 2.1.1
    ruby
    strace and tmux

Using strace, find out why Apache is returning a 500 error

 fix it and then automate it using Puppet

strace can attach to a current running process
You can use tmux to run strace in one window and curl in another one

puppet-lint 0-strace_is_your_friend.pp to check if the file meets the standard
