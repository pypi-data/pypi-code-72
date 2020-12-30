import argparse
import logging
import sys
from pathlib import Path

from oncoboxlib.quant.database import adjust_samples_for_db, load_database
from oncoboxlib.quant.scoring import calc_cnr, calc_pal
from oncoboxlib.quant.scoring.samples import load_samples

logger = logging.getLogger('oncoboxlib')


def parse_arguments(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--samples-file',
        help='File that contains cases (or cases and norms)',
        required=True
    )

    parser.add_argument(
        '--norms-file',
        help='File that contains norms'
    )

    parser.add_argument(
        '--samples-format',
        default='ngs counts',
        choices=['ngs counts', 'microarray expression'],
        help='Samples sequence format'
    )

    parser.add_argument(
        '--norm-averaging',
        default='gmean',
        choices=['gmean', 'mean'],
        help='Type of norms averaging'
    )

    parser.add_argument(
        '--databases-dir',
        help='Directory that contains databases',
        required=True
    )
    parser.add_argument(
        '--database-format',
        default='csv',
        choices=['csv', 'xlsx'],
        help='Type of databases format'
    )
    parser.add_argument(
        '--databases-names',
        default='all',
        help='Names of databased that uses for get PAL'
    )

    parser.add_argument(
        '--results-file',
        required=False,
        help='Output file that will contain results'
    )

    args = parser.parse_args(argv[1:] if argv else None)
    return args


def main(argv=None):
    args = parse_arguments(argv)

    databases_dir = Path(args.databases_dir)
    if not databases_dir.exists():
        raise ValueError(f'Databases path not found: {args.databases_dir}')

    if args.databases_names == 'all':
        databases_dirs = [d for d in databases_dir.iterdir() if d.is_dir()]
    else:
        databases_dirs = [d for d in databases_dir.iterdir() if d.is_dir() and d.name in args.databases_names]

    if not databases_dirs:
        raise ValueError('Not found any database.')

    # load cases and norms.
    # cases will be quantile normalized when set norms_file
    # samples must include norms when norms_file not set
    samples, norm_columns = load_samples(
        args.samples_file, args.norms_file, samples_format=args.samples_format)

    # get case-to-norm-ratio (cnr)
    cnr = calc_cnr(samples, norm_columns, args.norm_averaging)

    # load selected databases
    databases = [load_database(path, args.database_format) for path in databases_dirs]

    if args.results_file is None:
        results_file = Path(args.samples_file).absolute().parent / 'pal.csv'
    else:
        results_file = Path(args.results_file)
        results_file.parent.mkdir(exist_ok=True, parents=True)

    joined_pal = None
    for db in databases:
        adjusted_cnr = adjust_samples_for_db(cnr, db, 1.0)
        pal = calc_pal(adjusted_cnr, db.arr, db.gp)
        pal.insert(0, 'database', '{name} {version}'.format(**db.pathway_db))

        if joined_pal is None:
            joined_pal = pal
        else:
            joined_pal = joined_pal.append(pal)

    joined_pal.to_csv(results_file)

    logger.info(f'Calculation complete. Result -> {results_file}')


if __name__ == '__main__':
    logging_format = '%(asctime)s %(levelname)-8s %(name)-12s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=logging_format)
    logging.getLogger('oncoboxlib').setLevel(logging.DEBUG)

    main()
