main () {
    echo $@ | rev
}

main "$@"