// video-plugin.js
export default function createVideoPlugin() {
    return {
      install(VMdEditor) {
        VMdEditor.vMdParser.extendMarkdown(md => {
          // 视频解析规则
          const videoRegex = /^!\[video]\((.*?)\)$/;
  
          function videoTokenize(state, silent) {
            const start = state.pos;
            const max = state.posMax;
            const marker = state.src.charCodeAt(start);
  
            // 判断是否为![video](url)结构
            if (marker !== 0x21/* ! */ || start + 4 >= max) {
              return false;
            }
  
            if (state.src.charCodeAt(start + 1) !== 0x5B/* [ */) {
              return false;
            }
  
            const match = state.src.slice(start, max).match(videoRegex);
  
            if (!match || match.length < 2) {
              return false;
            }
  
            const url = match[1];
  
            if (!silent) {
              state.pos = start + match[0].length;
  
              const token = state.push('video', 'video', 0);
              token.attrs = [['src', url]];
              token.content = url;
            }
  
            return true;
          }
  
          md.inline.ruler.before('emphasis', 'video', videoTokenize);
  
          md.renderer.rules.video = function(tokens, idx) {
            const token = tokens[idx];
            const src = md.utils.escapeHtml(token.attrs[0][1]);
            return `<video class="vmd-video" controls src="${src}">Your browser does not support the video tag.</video>`;
          };
        });
      }
    };
  }