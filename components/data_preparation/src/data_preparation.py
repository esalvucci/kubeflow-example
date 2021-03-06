import pandas as pd
from electricity_consumption_dataset import ElectricityConsumptionDataset
from utility.singleton_logger import SingletonLogger
import fire

logger = SingletonLogger.get_logger()


def prepare_data(dataset_path):
    """
    Prepares the dataset to be used in the model training phase and save it in a local file as output.
    :param dataset_path - The path for the incoming dataset
    """
    output_path = '/tmp/dataset.csv'
    df = pd.read_csv(dataset_path)
    df = df.drop(columns="end").set_index("start")
    df.index = pd.to_datetime(df.index)
    df = df.groupby(pd.Grouper(freq="h")).mean()
    df.index.name = "time"
    electricity_consumption_dataset = ElectricityConsumptionDataset(df)
    dataset = electricity_consumption_dataset.get_transformed_dataset()
    if 'load' in df.columns:
        dataset['load'] = df['load']
    dataset.to_csv(output_path)
    logger.info("Dataset saved in " + output_path)


if __name__ == "__main__":
    fire.Fire(prepare_data)
