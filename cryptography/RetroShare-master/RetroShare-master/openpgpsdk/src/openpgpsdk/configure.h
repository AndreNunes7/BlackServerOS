/* generated by configure from include/openpgpsdk/configure.h.template. Don't edit. */

#define HAVE_ALLOCA_H 0
#define TIME_T_FMT	"%ld"

/* for silencing unused parameter warnings */
#define OPS_USED(x)	(x)=(x)

/* for tests, flag to tell gpg not to use blocking randomness */
#define GNUPG_QUICK_RANDOM "--quick-random"

/* Avoid a bunch of #ifs */
#ifndef O_BINARY
# define O_BINARY	0
#endif
