import os
from googleapiclient.http import MediaFileUpload
from Google import Create_Service


def export_csv_file(file_path: str, parents: list = None):
    """
        Function that takes in a file path and adds it to a google sheet
    """
    if not os.path.exists(file_path):
        print(f'{file_path} not found.')
        return
    try:
        file_metadata = {
            'name': os.path.basename(file_path).replace('.csv', ''),
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parent': parents
        }
        media = MediaFileUpload(filename=file_path, mimeType='text/csv')
        response = service.files().create(
            media_body=media,
            body=file_metadata
        ).execute()

        print(response)
        return response

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    csv_files = os.listdir('./CSV Files')

    for csv_file in csv_files:
        export_csv_file(os.path.join('CSV Files', csv_file))
        export_csv_file(os.path.join('CSV Files', csv_file), parents=['0AHXheLjvJGaQUk9PVA'])
