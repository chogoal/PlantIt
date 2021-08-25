import tempfile
import cv2
import requests
from django.db.models.fields import files
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from backgroundapp.models import Background


def background_get(request):
    access_key = 'd2O9LX_3cMvKvO8rrVdL_VMkirCrqI76DeP-INvUiBQ'
    image = f"https://api.unsplash.com/photos/random/?client_id={access_key}&query=nature&orientation=landscape&count=1"
    response = requests.get(image)
    photo = response.json()
    photo_dict = photo[0]
    image_url = photo_dict['urls']['raw']
    response_ = requests.get(image_url, stream=True)
    file_name = image_url.split('/')[3].split('?')[0] + '.jpg'
    tmp_img = tempfile.NamedTemporaryFile()

    new_background = Background()
    for block in response_.iter_content(1024 * 8):
        if not block:
            break
        tmp_img.write(block)

    new_background.image.save(file_name, files.File(tmp_img))

    temp = cv2.imread(new_background.image.url[1:])
    tem = cv2.resize(temp, (180, 72), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(tem, (5400, 2160), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(new_background.image.url[1:], output)

    return HttpResponse(cv2)


class BackgroundDetailView(DetailView):
    model = Background
    context_object_name = 'target_background'
    template_name = 'backgroundapp/detail.html'


class BackgroundListView(ListView):
    model = Background
    context_object_name = 'background_list'
    template_name = 'backgroundapp/list.html'
    paginate_by = 20
