# BgGPT for Jan 👋
[![Release](https://github.com/ivkos/jan-models-bggpt/actions/workflows/release.yml/badge.svg)](https://github.com/ivkos/jan-models-bggpt/actions/workflows/release.yml)

🤍💚❤️

Това репо предоставя JSON описания на българските езикови модели [**BgGPT**](https://bggpt.ai),
подходящи за инсталиране в чатбота [**Jan**](https://jan.ai).

[**Jan**](https://jan.ai) е алтернатива на ChatGPT, която може да се използва
локално и не изисква интернет връзка след сваляне на езиковите модели.


📥 В [релийзите](../../releases) на това репо ще намерите .zip файлове, които
съдържат JSON описания на моделите.


## Как да използвам тези модели в Jan?
1. Инсталирайте [Jan](https://jan.ai) на компютъра си, ако вече не сте го направили.
2. От [последния релийз](../../releases/latest) на това репо изтеглете .zip файла.
3. Разархивирайте съдържанието на .zip файла в директорията на Jan:
    - Linux и macOS: `~/jan/models`
    - Windows: `C:\Users\<your_user_name>\jan\models`
4. Рестартирайте Jan, ако в момента е стартиран.
5. От менюто **Hub** в Jan намерете и изтеглете избрания модел.

## Кой модел да избера?
BgGPT идва в няколко различни квантувани размера. Може да изберете модел, който
да отговаря на вашите нужди, като вземете предвид размера на диска и
изискването за VRAM.

ℹ️ По-малките модели в повечето случаи са по-бързи при по-малко
налична VRAM, но генерират по-некачествени резултати.


| Модел | Размер върху диска | Изискване за VRAM |
| --- | --- | --- |
| `Q4_K_S` | 4.17 GB | 5.21 GB  |
| `Q4_K_M` ✨ | 4.40 GB | 5.50 GB  |
| `Q5_K_S` ✨ | 5.03 GB | 6.29 GB  |
| `Q5_K_M` ✨ | 5.17 GB | 6.46 GB  |
| `Q6_K`   | 5.98 GB | 7.48 GB  |
| `Q8_0`   | 7.75 GB | 9.69 GB  |
| `F16`    | 14.6 GB | 18.25 GB |


> ✨ Препоръчани модели, базирани на [тази дискусия в llama.cpp](
    https://github.com/ggerganov/llama.cpp/discussions/2094
).
> VRAM = 1.25 * Disk

## Връзки
- [INSAIT @ Hugging Face](https://huggingface.co/INSAIT-Institute)
- [Jan @ GitHub](https://github.com/janhq/jan)
